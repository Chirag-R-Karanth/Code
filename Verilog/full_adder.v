module full_adder(
    output sum,cout,
    input a,b,cin
);
    wire x,y,z;
    xor(sum,a,b,cin);
    //display(sum);
    and(x,a,b);
    and(y,b,cin);
    and(z,a,cin);
    or(cout,x,y,z);
    //display(cout);
endmodule
