const result = document.querySelectorAll(".res")
const pts = document.querySelectorAll(".pts")
let points = 400
for (let i = 0;i < 11;i++){
    // console.log(result[0].textContent)
    if(result[i].textContent.includes('Correct')){
        console.log(result[i].textContent)
        result[i].style.color = 'Green'
    }else if (result[i].textContent.includes('Incorrect')){
        console.log(result[i].textContent)
        result[i].style.color = 'Red'

    }
}
let totalPoints = document.querySelector('#totalPoints')
let total_pts = 0
for (let i = 0;i < 10;i++){
    total_pts += parseInt(pts[i].textContent)
}

totalPoints.textContent = total_pts
