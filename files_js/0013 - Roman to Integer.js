/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(roman) {
    
let total = 0
for (let i=0; i<roman.length; i++) {
    if (roman[i] == "I") {
        if (roman[i+1] == "V") {
            total += 4
            i+=1
        } else if (roman[i+1] == "X") {
            total += 9
            i+=1
        } else {
            total += 1
        }
    }
    else if (roman[i] == "V") {
        total += 5
    }
    else if (roman[i] == "X") {
        if (roman[i+1] == "L") {
            total += 40
            i+=1
        } else if (roman[i+1] == "C") {
            total += 90
            i+=1
        } else {
            total += 10
        }
    }
    else if (roman[i] == "L") {
        total += 50
    }
    else if (roman[i] == "C") {
        if (roman[i+1] == "D") {
            total += 400
            i+=1
        } else if (roman[i+1] == "M") {
            total += 900
            i+=1
        } else {
            total += 100
        }
    }
    else if (roman[i] == "D") {
        total += 500
    }
    else if (roman[i] == "M") {
        total += 1000
    }
}
return total
};

inputs = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
for (let i = 0; i<inputs.length; i++){
    console.log(romanToInt(inputs[i]))
}
