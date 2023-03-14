function countDownFromTen() {
  function update(i) {
    document.getElementById("t").innerHTML = i;
    if (i-- > 0) setTimeout(() => update(i), 1000);
  }
  update(10);
}
