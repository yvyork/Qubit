
<div onclick="" class="card">
    <slot></slot>
</div>

<style>


.card {cursor: pointer;}
.card:hover {
  background: #d1e3f2 radial-gradient(circle, transparent 1%, #d1e3f2 1%) center/15000%;
}

.card {cursor: pointer;}
.card:active {
  background-color: #7fc0f2;
  background-size: 100%;
  transition: background 0s;
}

.card {
  background-position: center;
  transition: background 0.8s;
  border-radius: 15px;
  background-color: #fff;
  color: #333;
  border-radius: 15px;
  padding: 20px 50px;
  margin: 20px 0;
  position: relative;
}
</style>