const commaToArray = function (value) {
    return value.split(',')
                .filter(((word) => !!(word)))
                .map(a => a.trim());
}


export default commaToArray;