const result = document.querySelectorAll(".res")
let points = 400
for (let i = 0;i < 10;i++){
    // console.log(result[0].textContent)
    if(result[i].textContent.includes('Correct')){
        console.log(result[i].textContent)
        result[i].style.color = 'Green'
    }else if (result[i].textContent.includes('Incorrect')){
        console.log(result[i].textContent)
        result[i].style.color = 'Red'

    }
}
