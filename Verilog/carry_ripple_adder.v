module carry_ripple_adder(output [3:0] Sum,
    output Cout,
    input [3:0] A,B,
    input Cin );
        wire c1,c2,c3;
        full_adder FA1(Sum[0],c1,A[0],B[0],Cin);
        full_adder FA2(Sum[1],c2,A[1],B[1],c1);
        full_adder FA3(Sum[2],c3,A[2],B[2],c2);
        full_adder FA4(Sum[3],Cout,A[3],B[3],c3);
endmodule
