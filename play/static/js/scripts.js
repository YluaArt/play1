
async function fetchData(){
    try{    
        let res = await fetch("/get-data/");
        let resJs = await res.json();
        console.log(resJs);
        return true;
    }catch (error){
        console.error("Error ");
    }
    }
const coins = fetchData();
console.log(coins);
const div = document.createElement("div");
coins.array.forEach(element=> {
    div.innerHTML += `${element.name}<br>`

});
console.log(div);
