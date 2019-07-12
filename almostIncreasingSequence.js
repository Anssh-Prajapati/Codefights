function almostIncreasingSequence(sequence) {
    let strikes = 0;
    let max = Math.pow(-10, 5);
    let secondMax = Math.pow(-10, 5);
    
    sequence.map(elem =>{
        if(elem > max) {
            secondMax = max;
            max = elem;
        } else if(elem > secondMax) {
            max = elem;
            strikes++;
        } else strikes++;
    })
    
    return strikes <= 1;
}