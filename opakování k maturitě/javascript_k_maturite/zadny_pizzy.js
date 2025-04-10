// let pizzy = ["quattro formaggi", "hawaii", "margherita", "vegetariana", "prosciutto"]


// for (let i = 0; i < pizzy.length; i++) {
//     console.log(pizzy[i])
// }

// for (let i = 0; i < 10; i++) {
//     console.log("Žádné pizzy!")
// }


// for (const pizza of pizzy) {
//     console.log(pizza)
// }

// let x = 3
// let y = "3"

// if (x === y) {
//     console.log("3 rovnítka: Rovná se")
// } else {
//     console.log("3 rovnítka: Nerovná se")
// }


// if (x == y) {
//     console.log("2 rovnítka: Rovná se")
// } else {
//     console.log("2 rovnítka: Nerovná se")
// }


const nadpis = document.querySelector("#nadpis")
const tlacitko = document.querySelector(".tlacitko")
const tlacitko2 = document.querySelector(".tlacitko2")

tlacitko.addEventListener("click", function() {
    console.log("Funkce se spustila")
    nadpis.innerText = "Diskuze o Rakousku též zakázána!!!!"
    // nadpis.textContent = "Diskuze o Rakousku též zakázána"
    // nadpis.innerHTML = "Diskuze o Rakousku též zakázána"
    nadpis.style.fontSize = "100px"
    nadpis.style.color = "red"
    nadpis.classList.add("hokus")
})

// tlacitko.addEventListener("click", () => {
//     console.log("Funkce se spustila")
// })



// tlacitko.addEventListener("click", nejakaFunkce)

// function nejakaFunkce(){
//     console.log("Funkce se spustila")
// }

tlacitko2.addEventListener("click", function() {
    const input = document.querySelector(".input")
    console.log(input)
    console.log(input.value)
})

