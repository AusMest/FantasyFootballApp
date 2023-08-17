import axios from 'axios';
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

export default function Fetch(){
    const[data,setData] = useState([])
    var entires = []
    useEffect(()=>{
        getStats()
        stripData()
    },[])
    function getStats(){
        const url = "http://localhost:5000"
        axios.get(url).then((res)=>{
            //console.log(res)
            data.push(JSON.stringify(res.data))
            setData(JSON.stringify(res.data))
            console.log(data)
            localStorage.setItem("data",data)
            
            //console.log(data?.[0]?.[0].name)
        }).catch((err)=>{
            console.log(err)
        })
    }
    function stripData(){
        var tracker = {}
        if(JSON.parse(localStorage.getItem("data"))){
            console.log("it exists")
            tracker = JSON.parse(localStorage.getItem("data"));
        }
        document.getElementById('player_name').innerHTML = "Player Name: " ;
        document.getElementById('games_played').innerHTML = "Games Played: ";
        document.getElementById('completions').innerHTML = "Completions: ";
        document.getElementById('attempts').innerHTML = "Attempts: ";
        document.getElementById('completions_per').innerHTML = "Completions percentage: ";
        document.getElementById('season_yds').innerHTML = "Season Yards: ";
        document.getElementById('avg').innerHTML = "Average: ";
        document.getElementById('yards_per').innerHTML = "Yards per: ";
        document.getElementById('longest_pass').innerHTML = "Longest Pass: ";
        document.getElementById('touchdowns').innerHTML = "Touchdowns: ";
        document.getElementById('sacks').innerHTML = "Sacks: ";
        document.getElementById('interceptions').innerHTML = "Interceptions: ";
        document.getElementById('qb_rating').innerHTML = "QB Rating: ";
        for (var key in tracker) {
            console.log("data has cleared") 
            var name_ = document.createElement("p");
            name_.className = "name_";
            name_.innerHTML = tracker?.[key]?.[0].name;
            var games = document.createElement("p");
            games.className = "games_played";
            games.innerHTML = tracker[key]?.[0].touchdowns;
            var completions = document.createElement("p");
            completions.className = "completions";
            completions.innerHTML = tracker?.[key]?.[0].completions;
            var attempts = document.createElement("p");
            attempts.className ="attempts";
            attempts.innerHTML = tracker?.[key]?.[0].attempts;
            var comp_per = document.createElement("p");
            comp_per.className ="completions_per";
            comp_per.innerHTML = tracker?.[key]?.[0].completion_per;
            var season_yds = document.createElement("p");
            season_yds.className = "season_yards";
            season_yds.innerHTML = tracker?.[key]?.[0].season_yards;
            var avg = document.createElement("p");
            avg.className = "average";
            avg.innerHTML = tracker?.[key]?.[0].avg;
            var yards_per = document.createElement("p");
            yards_per.className = "yards_per";
            yards_per.innerHTML = tracker?.[key]?.[0].yards_per_game;
            var longest_pass = document.createElement("p");
            longest_pass.className = "longest_pass";
            longest_pass.innerHTML = tracker?.[key]?.[0].longest_pass;
            var touchdowns = document.createElement("p");
            touchdowns.className = "touchdowns";
            touchdowns.innerHTML = tracker?.[key]?.[0].touchdowns;
            var interceptions = document.createElement("p");
            interceptions.className = "interceptions";
            interceptions.innerHTML = tracker?.[key]?.[0].interceptions;
            var sacks = document.createElement("p");
            sacks.className ="sacks";
            sacks.innerHTML = tracker?.[key]?.[0].sacks;
            var qb_rating = document.createElement("p");
            qb_rating.className = "qb_rating";
            qb_rating.innerHTML = tracker?.[key]?.[0].qb_rating;
            if(tracker){
                document.getElementById('player_name').appendChild(name_);
                document.getElementById('games_played').appendChild(games);
                document.getElementById('completions').appendChild(completions);
                document.getElementById('attempts').appendChild(attempts);
                document.getElementById('completions_per').appendChild(comp_per);
                document.getElementById('season_yds').appendChild(season_yds);
                document.getElementById('avg').appendChild(avg);
                document.getElementById('yards_per').appendChild(yards_per);
                document.getElementById('longest_pass').appendChild(longest_pass);
                document.getElementById('touchdowns').appendChild(touchdowns);
                document.getElementById('interceptions').appendChild(interceptions);
                document.getElementById('sacks').appendChild(sacks);
                document.getElementById('qb_rating').appendChild(qb_rating);
            }
         }
    }
    
    return(
        <>
            <section id='quarters'>
                <p id='player_name'/><br/>
                <p id='games_played'> </p><br/>
                <p id='completions'> </p><br/>
                <p id='attempts'></p><br/>
                <p id='completions_per'></p><br/>
                <p id='season_yds'></p><br/>
                <p id='avg'></p><br/>
                <p id='yards_per'></p><br/>
                <p id='longest_pass'></p><br/>
                <p id='touchdowns'></p><br/>
                <p id='interceptions'></p><br/>
                <p id='sacks'></p><br/>
                <p id='qb_rating'></p><br/>  
                <Link to="/runners">Running Backs</Link>
            </section>
        </>
    )
}