state=Calc.getState();
let width = prompt("Line Width:");
for (index = 0; index < state.expressions.list.length; index++) {
   state.expressions.list[index].color="#000000"
   state.expressions.list[index].lines = "True"
   state.expressions.list[index].lineWidth =  width
   state.expressions.list[index].pointSize = "0"

}
Calc.setState(state);
