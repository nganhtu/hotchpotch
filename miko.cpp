/*Pham Tran Hoang Anh
lop: K63 DHCNTTA
Friday 27/10/2023*/
#include <iostream>
#include <string>
using namespace std;
struct SinhVien {
    string hoten;
    string lop;
    int sobaodanh;
    float diemtrungbinh;
    SinhVien* next;
};
SinhVien* taosinhvien(string hoten, string lop, int sobaodanh, float diemtrungbinh) {
    SinhVien* sv = new SinhVien;
    sv->hoten = hoten;
    sv->lop = lop;
    sv->sobaodanh = sobaodanh;
    sv->diemtrungbinh = diemtrungbinh;
    sv->next = NULL;
    return sv;
}
void themsinhvien(SinhVien*& head, SinhVien* sv) {
    if (head == NULL) {
        head = sv;
    } else {
        SinhVien* current = head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = sv;
    }
}
void nhapdanhsachsinhvien(SinhVien*& head, int n) {
    for (int i = 0; i < n; i++) {
        string hoten, lop;
        int sobaodanh;
        float diemtrungbinh;
        cout << "Nhap thong tin sinh vien thu " << i + 1 << ":" << endl;
        cout << "Ho ten: ";
        getline(cin, hoten);
        cout << "Lop: ";
        getline(cin, lop);
        cout << "So bao danh: ";
        cin >> sobaodanh;
        cout << "Diem trung binh: ";
        cin >> diemtrungbinh;
        cout << "---------------------\n";
        cin.ignore();
        SinhVien* sv = taosinhvien(hoten, lop, sobaodanh, diemtrungbinh);
        themsinhvien(head, sv);
    }
}
void loaibosinhvienkem(SinhVien*& head) {
    SinhVien* current = head;
    SinhVien* prev = NULL;
    while (current != NULL) {
        if (current->diemtrungbinh < 5) {
            if (prev == NULL) {
                head = current->next;
                delete current;
                current = head;
            } else {
                prev->next = current->next;
                delete current;
                current = prev->next;
            }
        } else {
            prev = current;
            current = current->next;
        }
    }
}
void indanhsachsinhvientheolop(SinhVien* head) {
    SinhVien* current = head;
    while (current != NULL) {
        cout << "Ho ten: " << current->hoten << endl;
        cout << "Lop: " << current->lop << endl;
        cout << "So bao danh: " << current->sobaodanh << endl;
        cout << "Diem trung binh: " << current->diemtrungbinh << endl;
        cout << "---------------------/n" << endl;
        current = current->next;
    }
}
void giaiphongbonho(SinhVien*& head) {
    SinhVien* current = head;
    while (current != NULL) {
        SinhVien* temp = current;
        current = current->next;
        delete temp;
    }
    head = NULL;
}
int main() {
    int n;
    cout << "Nhap so luong sinh vien: ";
    cin >> n;
    cin.ignore();
    SinhVien* danhSachSinhVien = NULL;
    nhapdanhsachsinhvien(danhSachSinhVien, n);
    loaibosinhvienkem(danhSachSinhVien);
    indanhsachsinhvientheolop(danhSachSinhVien);
    giaiphongbonho(danhSachSinhVien);
    return 0;
}
