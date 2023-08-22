import axios from 'axios';
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

export default function Runners(){
    const[data,setData] = useState([])
    var entires = []
    useEffect(()=>{
        getStats()
        setTitles()
        stripData()
    },[])
    function getStats(){
        const url = "http://localhost:5000/runners"
        axios.get(url).then((res)=>{
            //console.log(res)
            data.push(JSON.stringify(res.data))
            setData(JSON.stringify(res.data))
            console.log(data)
            localStorage.setItem("runners",data)
            
            //console.log(data?.[0]?.[0].name)
        }).catch((err)=>{
            console.log(err)
        })
    }
    function setTitles(){
        
        document.getElementById('player_name').innerHTML = "Player Name: " ;
        document.getElementById('games_played').innerHTML = "Games Played: ";
        document.getElementById('receptions').innerHTML = "Carries: ";
        document.getElementById('yards').innerHTML = "Yards: ";
        document.getElementById('avg_att').innerHTML = "Average/Att: ";
        document.getElementById('longest_run').innerHTML = "Longest Run: ";
        document.getElementById('twenty_yard_runs').innerHTML = "20+ Yard Runs: ";
        document.getElementById('touchdowns').innerHTML = "Touchdowns: ";
        document.getElementById('yards_game').innerHTML = "Yards per: ";
        document.getElementById('fumbles').innerHTML = "Fumbles: ";
        document.getElementById('fumbles_lost').innerHTML = "Fumbles Lost: ";
        document.getElementById('first_downs').innerHTML = "First Downs: ";
    }
    function stripData(){
        var tracker = {}
        if(JSON.parse(localStorage.getItem("runners"))){
            console.log("it exists")
            tracker = JSON.parse(localStorage.getItem("runners"));
        }
        

        for (var key in tracker) {
            console.log("data has cleared") 
            var name_ = document.createElement("p");
            name_.className = "name_";
            name_.innerHTML = tracker?.[key]?.[0].name;
            var games = document.createElement("p");
            games.className = "games_played";
            games.innerHTML = tracker[key]?.[0].games_played;
            var carries = document.createElement("p");
            carries.className = "carries";
            carries.innerHTML = tracker?.[key]?.[0].carries;
            var yards = document.createElement("p");
            yards.className ="yards";
            yards.innerHTML = tracker?.[key]?.[0].yards;
            var avg_att = document.createElement("p");
            avg_att.className ="avg_att";
            avg_att.innerHTML = tracker?.[key]?.[0].avg_att;
            var longest_run = document.createElement("p");
            longest_run.className = "longest_run";
            longest_run.innerHTML = tracker?.[key]?.[0].longest_run;
            var twenty_yard_runs = document.createElement("p");
            twenty_yard_runs.className = "twenty_yard_runs";
            twenty_yard_runs.innerHTML = tracker?.[key]?.[0].twenty_yard_runs;
            var yards_game = document.createElement("p");
            yards_game.className = "yards_game";
            yards_game.innerHTML = tracker?.[key]?.[0].yards_game;
            var touchdowns = document.createElement("p");
            touchdowns.className = "touchdowns";
            touchdowns.innerHTML = tracker?.[key]?.[0].touchdowns;
            var fumbles = document.createElement("p");
            fumbles.className = "fumbles";
            fumbles.innerHTML = tracker?.[key]?.[0].fumbles;
            var fumbles_lost = document.createElement("p");
            fumbles_lost.className ="fumbles_lost";
            fumbles_lost.innerHTML = tracker?.[key]?.[0].fumbles_lost;
            var first_downs = document.createElement("p");
            first_downs.className = "first_downs";
            first_downs.innerHTML = tracker?.[key]?.[0].first_downs;
            if(tracker){
                document.getElementById('player_name').appendChild(name_);
                document.getElementById('games_played').appendChild(games);
                document.getElementById('receptions').appendChild(carries);
                document.getElementById('targets').appendChild(yards);
                document.getElementById('yards').appendChild(avg_att);
                document.getElementById('average').appendChild(longest_run);
                document.getElementById('touchdowns').appendChild(twenty_yard_runs);
                document.getElementById('longest_catch').appendChild(touchdowns);
                document.getElementById('20_plus_yard_catches').appendChild(yards_game);
                document.getElementById('yards/game').appendChild(fumbles);
                document.getElementById('fumbles').appendChild(fumbles_lost);
                document.getElementById('fumbles_lost').appendChild(first_downs);
                document.getElementById('yards_after_catch').appendChild(first_downs);
                document.getElementById('first_downs').appendChild(first_downs);

            
            }
         }
    }
    
    return(
        <>
            <section id='runners'>
                <p id='player_name'/><br/>
                <p id='games_played'> </p><br/>
                <p id='receptions'> </p><br/>
                <p id='targets'></p><br/>
                <p id='yards'></p><br/>
                <p id='average'></p><br/>
                <p id='touchdowns'></p><br/>
                <p id='longest_catch'></p><br/>
                <p id='20_plus_yard_catches'></p><br/>
                <p id='yards/game'></p><br/>
                <p id='fumbles'></p><br/>
                <p id='fumbles_lost'></p><br/>
                <p id='yards_after_catch'></p><br/>
                <p id='first_downs'></p><br/>
                <Link to="/">Quarterbacks</Link>
                <Link to="/runners">Running Backs</Link>
            </section>
            

        </>
    )
}