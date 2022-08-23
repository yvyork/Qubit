<script>
    import TicketItem from "./TicketItem.svelte";

    export let list;
</script>

<div class="py-4 grid gap-4 grid-cols-1 w-auto">
    {#each $list as tk }
    <TicketItem item={tk} on:aufrufen />
    {/each}
</div>
