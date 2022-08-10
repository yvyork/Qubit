<script>
    import Card from '../components/Card.svelte';
    import { counter } from '../stores/counterstore';

    export let ticketType;

    let local = "127.0.0.1";
	let server = "165.22.94.223";

    let url = 'http://165.22.94.223:8000/queue/ticket/'

    async function handleSubmit() {

        const submit = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                wait: ticketType.wait_time,
                counter: counterId(),
            })
        });
        const data = await submit.json();
    }

    function counterId() {
        return $counter === 'Schalter A' ? 1 : 2;
    }
    
</script>

<Card>
    <div class="frame">
    <button class="h-20 w-96" id="ripple" on:click={handleSubmit}>
        <div class="flex flex-row justify-center">
            <div class="px-7 text-4xl font-bold text-center">{ticketType.wait_time} min</div>
        </div>
    </button>
</div>
</Card>

<style>

</style>