<script>
	import { counter } from "../stores/counterstore";
	import Card from "../components/Card.svelte";

	function setCounter1() {
		var counterName = document.getElementById("counter1").innerText;
		setLocalCounter(counterName);
	}

	function setCounter2() {
		var counterName = document.getElementById("counter2").innerText;
		setLocalCounter(counterName);
	}

	// function setCounter3() {
	// 	var counterName = document.getElementById("counter3").innerText;
	// 	setLocalCounter(counterName);
	// }

	function setLocalCounter(counterId) {
		// localStorage.clear();
		$counter = counterId;
	}
</script>


<div class="counter-links">
	<div class="flex flex-col mx-auto">
		<div class="card-item">
			<Card>
				<a href="/queue" class="counter" id="counter1" on:click={setCounter1}>Schalter 1</a>
			</Card>
		</div>
		<div>
			<Card class="card-item">
				<a href="/queue" class="counter" id="counter2" on:click={setCounter2}>Schalter 2</a>
			</Card>
		</div>
		<!-- <div>
			<Card class="card-item">
				<a href="/queue" class="counter" id="counter3" on:click={setCounter3}>Schalter 3</a>
			</Card>
		</div> -->
		<div>
			<Card class="card-item">
				<a href="/register" class="counter">Registrierung</a>
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
</style>