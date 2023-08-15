import axios from 'axios';
import { useEffect, useState } from 'react';

export default function Fetch(){
    const[data,setdata] = useState([])
    var entries = []

    useEffect(()=>{
        getStats()
        stripData()
    },[])
    function getStats(){
        const url = "http://localhost:5000"
        axios.get(url).then((res)=>{
            console.log(res)
            setdata(res.data)
            console.log(data?.[0]?.[0].name)
        }).catch((err)=>{
            console.log(err)
        })
    }
    function stripData(){
        document.getElementById('player_name').innerHTML = "Player Name: ";
        document.getElementById('games_played').innerHTML = "Games Played: ";
        document.getElementById('completions').innerHTML = "Completions: ";


        var count = 0;

        for (var key in data) { 
            var name_ = document.createElement("p");
            name_.className = "name_";
            name_.innerHTML = data?.[key]?.[0].name;
            var games = document.createElement("p");
            games.className = "games_played";
            games.innerHTML = data?.[key]?.[0].touchdowns;
            var completions = document.createElement("p");
            completions.className = "completions";
            completions.innerHTML = data?.[key]?.[0].completions
            if(data){
                document.getElementById('player_name').appendChild(name_);
                document.getElementById('games_played').appendChild(games);
                document.getElementById('completions').appendChild(completions);

            }
            count = count + 1;
      
         }
        
    }
    
    
    return(

        <>
              
            <div className='stats'>
                <p id='player_name'/>
                <br/>
                <p id='games_played'> </p><br/>
                <p id='completions'> </p><br/>
                <p> Attempts: {data.attempts}</p><br/>
                <p> Completions Per: {data.completion_per}</p><br/>
                <p> Season Yards: {data.season_yards}</p><br/>
                <p> Average: {data.avg}</p><br/>
                <p> Yards Per Game: {data.yards_per_game}</p><br/>
                <p> Longest pass:{data.longest_pass}</p><br/>
                <p> Touchdowns: </p><br/>
                <p> Interceptions: {data.interceptions}</p><br/>
                <p> Sacks: {data.sacks}</p><br/>
                <p> QB Rating: {data.qb_rating}</p><br/>
                    
            </div>


        </>
    )
}