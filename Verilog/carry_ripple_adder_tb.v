`timescale 1ns/1ps

module carry_ripple_adder_tb;

    wire [3:0] Sum;
    wire Cout;

    reg [3:0] A, B;
    reg Cin;

    // Instantiate the DUT (Device Under Test)
    carry_ripple_adder uut (
        .A(A),
        .B(B),
        .Cin(Cin),
        .Sum(Sum),
        .Cout(Cout)
    );

    initial begin
        $dumpfile("carry_ripple_adder.vcd");
        $dumpvars(0, carry_ripple_adder_tb);

        // Test cases
        A = 4'b0000; B = 4'b0000; Cin = 0; #10;
        A = 4'b0001; B = 4'b0001; Cin = 0; #10;
        A = 4'b0010; B = 4'b0011; Cin = 0; #10;
        A = 4'b1111; B = 4'b0001; Cin = 0; #10;
        A = 4'b1010; B = 4'b0101; Cin = 1; #10;
        A = 4'b1111; B = 4'b1111; Cin = 1; #10;
        $finish;
    end
endmodule
