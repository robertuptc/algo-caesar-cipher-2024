function caesarCipher(str, shift_amount) {
    checking_char(str, shift_amount)
};

function checking_char(str, shift_amount){
    let char_only = /^[a-zA-Z]+$/;
    let answer = ""

    for (let i = 0; i < str.length; i++) {
        if (str[i] == ' ') {
            answer += ' '
        } else if (!char_only.test(str[i])) {
            answer += str[i]
        } else {
            answer += shifting(str, i, shift_amount, 122, 97)
        }
    }
    console.log(answer)
    return answer
}

function shifting(str, i, shift_amount, max_char_code, min_char_code){
    let isUpper = str[i] == str[i].toUpperCase()
    let answer = ''
    str = str.toLowerCase()

    if (shift_amount < 0) {
        if (str.charCodeAt(i) + shift_amount < min_char_code) {
            answer = String.fromCharCode((max_char_code + 1) + (shift_amount + (str.charCodeAt(i) - min_char_code)))
            return isUpper ? answer.toUpperCase() : answer
        } else {
            answer = String.fromCharCode(str.charCodeAt(i) + shift_amount)
            return isUpper ? answer.toUpperCase() : answer
        }

    } else if (shift_amount > 0) {
        if (str.charCodeAt(i) + shift_amount > max_char_code) {
            answer = String.fromCharCode((min_char_code - 1) + (shift_amount - (max_char_code - str.charCodeAt(i))))
            return isUpper ? answer.toUpperCase() : answer
        } else {
            answer = String.fromCharCode(str.charCodeAt(i) + shift_amount)
            return isUpper ? answer.toUpperCase() : answer
        }
    }
}
module.exports = {caesarCipher}