<script>
    import TicketItem from "./TicketItem.svelte";
    import {currentTicket} from "../stores/ticketstore"
    import {counter} from "../stores/counterstore"
    import { fade } from 'svelte/transition';
</script>

<h1 id="serving" class="text-4xl text-center my-7 uppercase"><strong>
    {#if $counter == undefined} Bitte Schalter auswählen {:else}  {$counter} {/if}</strong></h1>


<div class="py-4 grid gap-4 grid-cols-1 w-auto">
    <div class="max-w-lg mx-auto">
    {#if $currentTicket}
    <TicketItem item={$currentTicket} showButton={false}/>
    {/if}
    </div>
</div>
    
<style>
    #serving {
        color: white;
    }
</style>


