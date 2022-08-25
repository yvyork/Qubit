<script>
import TicketForm from "../components/TicketForm.svelte";

    const ticketTypes = [
        {
            "wait_time": 5
        },
        {
            "wait_time": 15
        },
        {
            "wait_time": 30
        },
    ]

</script>


<svelte:head>
    <title>Registrierung</title>
</svelte:head>

<div class="thing">
    <h1 class="text-4xl text-center my-8 uppercase">Registrierung</h1>
    <!-- <h1 class="text-center text-2xl">Registriere ein neues Ticket hier</h1> -->

</div>

<div class="mx-auto max-w-lg">
    <div class="py-4 grid gap-x-8 gap-y-4 grid-cols-1 w-auto">
        {#each ticketTypes as ticketItem}
        <TicketForm ticketType={ticketItem} />
        {/each}
    </div>    
</div>



<style>
    .thing {
        font-family: 'Poppins', sans-serif;
        color: white;
    }
</style>