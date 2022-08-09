<script>
    import TicketItem from "./TicketItem.svelte";
    import {waitinglist} from "../stores/ticketstore"
</script>

<div class="py-4 grid gap-4 grid-cols-1 w-auto">
    {#each $waitinglist as tk }
    <TicketItem item={tk} on:aufrufen />
    {/each}
</div>
