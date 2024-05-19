let hrs_el = document.querySelector('#hrs')
let mins_el = document.querySelector('#mins')
let secs_el = document.querySelector('#secs')
function timeleft() {
    let date = new Date()
    const starttime = 10*3600
    let seconds = date.getSeconds()
    let mins = date.getMinutes() *60
    let hours = date.getHours() *3600
    let left0= (seconds+mins+hours) - starttime
    let left = 7200 - left0
    let hrs = Math.floor(left / 3600)
    let mins1 = Math.floor((left-(hrs*3600) )/60)
    let secs = Math.floor((left -(hrs * 3600 + mins1*60) ))
    if (mins1<10){
        mins1 = '0' + mins1
    }if (secs<10){
        secs = '0' + secs
    }
    hrs_el.textContent = '0'+hrs + ":"
    mins_el.textContent = mins1 + ":"
    secs_el.textContent = secs
    // console.log( [hrs,mins1,secs])
}


setInterval(timeleft,100)