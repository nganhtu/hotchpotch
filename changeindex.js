var changeIdxInArr = (arr, oldIdx, newIdx) => {
    while (oldIdx < 0) {
        oldIdx += arr.length;
    }
    while (newIdx < 0) {
        newIdx += arr.length;
    }
    if (newIdx >= arr.length) {
        let k = newIdx - arr.length + 1;
        while (k--) {
            arr.push(undefined);
        }
    }
    arr.splice(newIdx, 0, arr.splice(oldIdx, 1)[0]);
    return arr; // for testing purpose
};
