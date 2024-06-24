// const { caesarCipher } = require("./caesarCipher")

const cs = require("./caesarCipher")

describe("Testing positive shift", () => {
    test("Tests caesarCipher(here5, 5) is mjwj5", () => {
        const result = cs.caesarCipher("hello5", 5)
        expect(result).toBe("mjwj5")
    })
})