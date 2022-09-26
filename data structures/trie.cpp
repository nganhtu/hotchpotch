#include <string>

#define ALPHABET_SIZE 26

int ctoi(char c) {
    return c - 'a';
}

char itoc(int i) {
    return 'a' + i;
}

struct Node {
    int end;
    Node *next[ALPHABET_SIZE];

    Node() {
        end = 0;
        for (int i = 0; i < ALPHABET_SIZE; ++i) {
            next[i] = nullptr;
        }
    }
};

void add(Node *head, std::string s) {
    if (s == "") {
        head->end++;
        return;
    }

    Node *ptr = head;
    for (int i = 0; i < s.length(); ++i) {
        if (ptr->next[ctoi(s[i])] == nullptr) {
            ptr->next[ctoi(s[i])] = new Node();
        }
        ptr = ptr->next[ctoi(s[i])];
        if (i == s.length() - 1) {
            ptr->end++;
        }
    }
}

int find(Node *head, std::string s) {
    if (s == "") {
        return head->end;
    }

    Node *ptr = head;
    for (int i = 0; i < s.length(); ++i) {
        if (ptr->next[ctoi(s[i])] == nullptr) {
            return 0;
        }
        ptr = ptr->next[ctoi(s[i])];
        if (i == s.length() - 1) {
            return ptr->end;
        }
    }

    return -1;
}

/**
 * Normally when using trie, we don't need to delete any string.
 * It can be done easily by reduce end attribute by 1.
 * But using that way will waste memory.
 */
