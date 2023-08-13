const phrase="6c7974786c79676d636c776d6a7a7263"
const CryptoJS = require ("crypto-js");
function getPedoc()
{
    let pedoc = ""
    for(let i=0;i<phrase.length/2;i++){
        let code=phrase.substr(2*i,2)
        code = hex2int(code)
        let char=String.fromCharCode(code);
        pedoc = char+pedoc
    }
    return pedoc;
}

function hex2int(hex) {
    var len = hex.length, a = new Array(len), code;
    for (var i = 0; i < len; i++) {
        code = hex.charCodeAt(i);
        if (48<=code && code < 58) {
            code -= 48;
        } else {
            code = (code & 0xdf) - 65 + 10;
        }
        a[i] = code;
    }
    return a.reduce(function(acc, c) {
        acc = 16 * acc + c;
        return acc;
    }, 0);
}
function jbbbbbb (word,) { // 加密
var  keyStr='crzjmwlcmgylxtyl'
var key = CryptoJS.enc.Utf8.parse(keyStr)

var srcs = CryptoJS.enc.Utf8.parse(word)

var jbbbbbbed = CryptoJS.AES.encrypt(srcs, key, {mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7}) // 加密模式为ECB，补码方式为PKCS5Padding（也就是PKCS7）

return jbbbbbbed.toString()

}

function jaaaaaaaa (word, keyStr) { // 解密

var key = CryptoJS.enc.Utf8.parse(keyStr)

var jaaaaaaaa = CryptoJS.AES.decrypt(word, key, {mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7})

return CryptoJS.enc.Utf8.stringify(jaaaaaaaa).toString()

}
data=
'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'
function jiemi (data){
     return jaaaaaaaa(data, getPedoc())}
console.log(jiemi(data))
// console.log(res)
// jia=jbbbbbb('日')
// console.log(jia)