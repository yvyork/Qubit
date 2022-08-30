<script>
    import Card from '../components/Card.svelte';

    export let ticketType;

    let server = "10.65.15.141";
    let local = "127.0.0.1";

    let idcounter = 2;
    let url = `http://${local}:8000/queue/ticket/`

    async function handleSubmit() {

        const submit = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                id: idcounter,
                wait: ticketType.wait_time,
            })
        });
        const data = await submit.json();
        idcounter++;
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
