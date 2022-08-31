<script>
    import TicketItem from "./TicketItem.svelte";
    import {currentTicket} from "../stores/ticketstore"
    import {counter} from "../stores/counterstore"

    
    const callAgain = async (e) => {
        // const url_pacs = "http://10.65.15.141:3100/api/rank";
        const url = "http://10.65.15.159:3100/api/rank";
        let ticket = e.detail;
        const res = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({
                "ticket": "# " + ticket.number,
                "room": $counter,
            })
            
        })
    }

</script>

<h1 id="serving" class="text-4xl text-center my-7 uppercase"><strong>
    {#if $counter == undefined} Bitte Schalter auswählen {:else}  {$counter} {/if}</strong></h1>


<div class="py-4 grid gap-4 grid-cols-1 w-auto">
    <div class="max-w-lg mx-auto">
    {#if $currentTicket}
    <TicketItem item={$currentTicket} showButton={false} callAgainButton={true} on:call-again={callAgain}/>
    {/if}
    </div>
</div>
    
<style>
    #serving {
        color: white;
    }
</style>


