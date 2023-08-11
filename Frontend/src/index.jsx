import React, { useState, useEffect } from "react";
import { Component } from "react";
import {render} from 'react-dom';
export default function Fantasy() {
    

    function FantasyList (){
    // usestate for setting a javascript
    // object for storing and using data
        const [data, setdata] = useState({
            name: "",
            games_played:0,
            completions:0,
            attempts:0,
            completion_per:0,
            season_yards:0,
            avg:0,
            yards_per_game:0,
            longest_pass:0,
            touchdowns: 0,
            interceptions:0,
            sacks:0,
            qb_rating:0

        });
    
 
    // Using useEffect for single rendering
    useEffect(()=>{
        // Using fetch to fetch the api from
        // flask server it will be redirected to proxy
        fetch("http://localhost:5000/").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                this.setdata({
                    name:           data.name,
                    games_played:   data.games_played,
                    completions:    data.completions,
                    attempts:       data.attempts,
                    completion_per: data.completion_per,
                    season_yards:   data.season_yards,
                    avg:            data.avg,
                    yards_per_game: data.yards/g,
                    longest_pass:   data.longest_pass,
                    touchdowns:     data.touchdowns,
                    interceptions:  data.interceptions,
                    sacks:          data.sacks,
                    qb_rating:      data.qb_rating,
                })
                .catch(rejected =>{console.log(rejected)});
            })
        );
    })
        return(
        <div className="App" >
            <header className="App-header">
                <h1>Players List Goes Here</h1>
                {/* Calling a data from setdata for showing*/}
                <p>{data.name}</p>
                <p>{data.games_played}</p>
                <p>{data.completions}</p>
                <p>{data.attempts}</p>
                <p>{data.completion_per}</p>
                <p>{data.season_yards}</p>
                <p>{data.avg}</p>
                <p>{data.yards_per_game}</p>
                <p>{data.longest_pass}</p>
                <p>{data.touchdowns}</p>
                <p>{data.interceptions}</p>
                <p>{data.sacks}</p>
                <p>{data.qb_rating}</p>
            </header>
        </div>
        )}
}
