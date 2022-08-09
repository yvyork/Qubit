<script>
	import { counter } from "../stores/counterstore";
	import Card from "../components/Card.svelte";

	function setCounterA() {
		var counterName = document.getElementById("counterA").innerText;
		setLocalCounter(counterName);
	}

	function setCounterB() {
		var counterName = document.getElementById("counterB").innerText;
		setLocalCounter(counterName);
	}

	function setLocalCounter(counterId) {
		$counter = counterId;
	}
</script>


<div class="counter-links">
	<div class="flex flex-col mx-auto">
		<div class="card-item">
			<Card>
				<a href="/queue" class="counter" id="counterA" on:click={setCounterA}>Schalter A</a>
			</Card>
		</div>
		<div>
			<Card class="card-item">
				<a href="/queue" class="counter" id="counterB" on:click={setCounterB}>Schalter B</a>
			</Card>
		</div>
		
	</div>
</div>


<style>
	.counter-links {
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		align-items: center;
		flex-wrap: wrap;
		margin-top: 80px;
	}
	/* .card-item {
		margin: 10px;
	} */

	.counter {
		font-size: 30px;
		font-weight: bold;
		padding: 10px;
		text-align: center;
	}
	
	.counter:hover {
		background-color: #fff;
		color: #000;
	}
</style>