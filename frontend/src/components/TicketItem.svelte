<script>
    import Card from './Card.svelte'
    import {createEventDispatcher} from 'svelte'
    import { counter } from '../stores/counterstore';
    export let item
    export let showButton = true;

    const dispatch = createEventDispatcher()
    const handleCall = (item) => {
        dispatch('aufrufen', item);      
    } 

    function time_difference() { return Math.ceil((Date.now() - Date.parse(item.timestamp)) / 60000);}

    let time_counter = 0;
    
    setInterval (() => {
        time_counter = time_difference();
    }, 1500);
</script>

<Card>
    <!-- Red Time Counter --> 
    <div class="time-display" >{time_counter}</div>
    <!-- Genereal Ticket Info -->
    <div class="flex flex-row justify-around"> 
        <div class="px-4 font-bold text-4xl">{item.number}</div>
        <!-- <div class="w-3"></div> -->
        <div class="px-4 text-4xl">{item.wait} min</div>
        {#if showButton}
        <button class="call-button" on:click={() => handleCall(item)}>Aufrufen</button>
        {/if}
    </div>       
</Card>

<style>
        .time-display {
        position: absolute;
        top: -10px;
        left: -10px;
        width: 50px;
        height: 50px;
        background: #ff6a95;
        color: #fff;
        border: 1px #eee solid;
        border-radius: 50%;
        padding: 10px;
        text-align: center;
        font-size: 19px;
    }

    .call-button {
        background-color: #FFFFFF;
        border: 1px solid rgb(209,213,219);
        border-radius: .5rem;
        box-sizing: border-box;
        color: #111827;
        line-height: 1.25rem;
        padding: .75rem 1rem;
        text-align: center;
        text-decoration: none #D1D5DB solid;
        font-weight: bold;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        cursor: pointer;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;    
    }


</style>