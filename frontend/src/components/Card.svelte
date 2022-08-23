
<div class="card">
    <slot></slot>
</div>

<style>

  /* Ripple effect */
  .card {
  background-position: center;
  transition: background 0.8s;
  border-radius: 15px;
}
.card:hover {
  background: #d1e3f2 radial-gradient(circle, transparent 1%, #d1e3f2 1%) center/15000%;
}
.card:active {
  background-color: #cae0f1;
  background-size: 100%;
  transition: background 0s;
}

    .card {
  background-color: #fff;
  color: #333;
  border-radius: 15px;
  padding: 20px 50px;
  margin: 20px 0;
  position: relative;
}
</style>