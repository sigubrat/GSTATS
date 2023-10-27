<script setup>
import axios from 'axios'
import config from '@/config.js'
import PlayerCard from './components/PlayerCard.vue';

/* Get the last time the player connected to the server using an api POST call
 url: https://growlingonline.com:9000/stats/search
 payload: nick=config.playerName&date=null
*/

const headers = {
  'Content-Type': 'multipart/form-data',
}

const placeholderStats = {
    "deaths": 30,
    "aakills": 51,
    "aakdr": 1.7,
    "lastSessionKills": 0,
    "lastSessionDeaths": 1,
    "killsByModule": [
        {
            "module": "F-16C_50",
            "kills": 51
        }
    ],
    "kdrByModule": [
        {
            "module": "F-16C_50",
            "kdr": 1.7
        }
    ]
}

const getLastConnected = async () => {
  const formData = new FormData();
  formData.append('nick', config.playerName);
  formData.append('date', null);
  try {
    const response = await axios.post('http://localhost:8000/', formData)
    console.log(response)
  } catch (error) {
    console.error(error);
    console.log("Providing placeholder value")
    return "2023-10-26T17:46:43.943655";
  }
}

const getStats = async () => {
  const formData = new FormData();
  formData.append('nick', config.playerName);
  formData.append('date', '2023-10-27T11:54:41.188505');
  try {
    const response = await axios.post('http://localhost:8000/', formData)
    console.log(response)
    return response
  } catch (error) {
    console.error(error);
    console.log("Providing placeholder value")
    return placeholderStats;
  }
}

let lastConnected = getLastConnected();
let stats = getStats();

</script>

<template>
  <main>
    <PlayerCard :player="config.playerName" lastCon="2023-10-26T17:46:43"/>
  </main>
</template>

<style scoped>

</style>
