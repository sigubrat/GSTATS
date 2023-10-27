<script setup>
defineProps({
  player: {
    type: String,
    required: true
  },
  lastCon: {
    type: [String, null, Object, Promise],
    required: true
  },
})

</script>

<script>
function formatDate(date) {
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
    const d = new Date(date)
    return d.toLocaleDateString(undefined, options)
}
</script>

<template>
    <div class="wrapper">
        <!-- F-16 img from assets folder -->
        <img src="../assets/img/f-16.jpg" alt="F-16">
        <div class="overlay-text">
            <h2 class="player-name">{{ player }}</h2>
            <span>Played: {{ formatDate(lastCon) }} </span>
        </div>
    </div>
</template>

<style scoped>

    .wrapper {
        position: relative;
        max-height: 800px;
        max-width: 600px;
        border-radius: 15px;
        overflow: hidden;
    }

    img {
        max-width: 100%;
        max-height: 100%;
        object-fit: cover;
    }

    .wrapper .overlay-text {
        position: absolute;
        top: 85%;
        z-index: 1;
        color: white;
        display: flex;
        align-content: center;
        justify-content: space-around;
        flex-direction: row;
        align-items: baseline;
        width: 60%;
    }

    .player-name  {
        font-weight: bold;
    }
</style>
