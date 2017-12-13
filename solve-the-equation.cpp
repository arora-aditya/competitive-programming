class Solution {
public:
    enum State{left, equal,right}
    enum Var{x,num,sign}
    struct side{
        int x;
        int num;
        side{
            x = 0;
            num = 0;
        }
    }
    string solveEquation(string equation) {
        int i = 0;
        State state = left;
        Var var;
        side left,right;
        while(equation[i] != '\0'){
            switch(state){
                case left:
                    if(equation[i] == '+' && var != sign){
                        var = sign;
                        sign = 1;
                    }
                    else{
                        return "No solution"
                    }
                    switch(var){
                        case sign:
                            if(equation[i-1] == '+'){
                                sign = 1;
                            }
                            else if(equation[i-1] == '-'){
                                sign = -1;
                            }
                            if()
                        case x:
                        case sign:
                    }
            }
            i++;
        }
    }
};
