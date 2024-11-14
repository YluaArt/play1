async function fetchData(){

    try{    
        let res = await fetch("https://api.coinlore.net/api/tickers/");
        let resJs = await res.json();
        console.log(resJs);
    }catch (error){
        console.error("Error ");
    }
    }
    fetchData() 
    alert("end");