var valor;
function botao(value){
	valor = document.calc.visor.value += value;
}

function reset(){
	document.calc.visor.value = '';
}
function calcula(){
	document.calc.visor.value = eval(document.calc.visor.value);
}
