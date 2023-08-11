import axios from 'axios';
import { useEffect, useState } from 'react';

export default function Fetch(){
    const[data,setdata] = useState([])
            

    useEffect(()=>{
        getStats()
    },[])
    function getStats(){
        const url = "http://localhost:5000"
        axios.get(url).then((res)=>{
            console.log(res)
            setdata(res.data)
        }).catch((err)=>{
            console.log(err)
        })
    }
    
    return(
        <>
            <div className='stats'>
                <p>Player Name: {data.name} </p>
                <br/>
                <p> Games Played: {data.games_played} </p><br/>
                <p> Completions: {data.completions}</p><br/>
                <p> Attempts: {data.attempts}</p><br/>
                <p> Completions Per: {data.completion_per}</p><br/>
                <p> Season Yards: {data.season_yards}</p><br/>
                <p> Average: {data.avg}</p><br/>
                <p> Yards Per Game: {data.yards_per_game}</p><br/>
                <p> Longest pass:{data.longest_pass}</p><br/>
                <p> Touchdowns: {data.touchdowns}</p><br/>
                <p> Interceptions: {data.interceptions}</p><br/>
                <p> Sacks: {data.sacks}</p><br/>
                <p> QB Rating: {data.qb_rating}</p><br/>
            </div>


        </>
    )
}