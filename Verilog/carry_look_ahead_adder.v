`timescale 1ns/1ps
// ---------------------------------------------------------------
// 4-bit Carry-Look-Ahead Adder
// ---------------------------------------------------------------
module carry_look_ahead_adder (
    input  [3:0] a,      // operand A
    input  [3:0] b,      // operand B
    input        cin,    // carry in
    output [3:0] sum,    // sum
    output       cout    // carry out
);

    // -------------------------------------------------------
    // Generate (g) and Propagate (p) signals
    // -------------------------------------------------------
    wire [3:0] g = a & b;               // g_i = a_i * b_i
    wire [3:0] p = a ^ b;               // p_i = a_i + b_i  (xor)

    // -------------------------------------------------------
    // Internal carry wires
    // -------------------------------------------------------
    wire c0, c1, c2, c3, c4;   // c0 = cin, c4 = cout

    assign c0 = cin;

    assign c1 = g[0] | (p[0] & c0);
    assign c2 = g[1] | (p[1] & g[0]) | (p[1] & p[0] & c0);
    assign c3 = g[2] | (p[2] & g[1]) | (p[2] & p[1] & g[0]) |
                (p[2] & p[1] & p[0] & c0);
    assign c4 = g[3] | (p[3] & g[2]) | (p[3] & p[2] & g[1]) |
                (p[3] & p[2] & p[1] & g[0]) |
                (p[3] & p[2] & p[1] & p[0] & c0);

    assign cout = c4;

    // -------------------------------------------------------
    // Sum = p xor carry
    // -------------------------------------------------------
    assign sum = p ^ {c3,c2,c1,c0};

endmodule
