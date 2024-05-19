const result = document.querySelectorAll(".res")
const pts = document.querySelectorAll(".pts")
const questionlink = document.querySelectorAll('.links')
let points = 400
for (let i = 0;i < 11;i++){
    // console.log(result[0].textContent)
    if(result[i].textContent.includes('Correct')){
        console.log(result[i].textContent)
        result[i].style.color = 'Green'
        // questionlink[i].href = '#'
        questionlink[i].setAttribute('pointer-events','none')
        questionlink[i].setAttribute('display','inline-block')
    }else if (result[i].textContent.includes('Incorrect')){
        console.log(result[i].textContent)
        result[i].style.color = 'Red'

    }
}
let totalPoints = document.querySelector('#totalPoints')
function adding(){
    let total_pts = 0
    for (let i = 0;i < 10;i++){
    total_pts += parseInt(pts[i].textContent)
    console.log(total_pts)
    totalPoints.textContent = total_pts
}}
setInterval(adding,1000)

