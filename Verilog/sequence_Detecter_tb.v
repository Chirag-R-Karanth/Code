`timescale 1ns/1ps

module sequence_Detecter_tb ();

  reg a;
  reg clk;
  reg reset;
  wire q;

  // Instantiate the DUT (Device Under Test)
  sequence_Detecter dut (
    .a(a),
    .clk(clk),
    .reset(reset),
    .q(q)
  );

  // Clock generation (10 ns period)
  always #5 clk = ~clk;

  initial begin
    // Initialize signals
    clk = 0;
    a = 0;
    reset = 1;

    // Dump waveform
    $dumpfile("seqdet.vcd");
    $dumpvars(0, sequence_Detecter_tb);

    // Apply reset
    #12 reset = 0;

    // Input sequence: 1 0 1 0 1 1 0 1
    #10 a = 1;
    #10 a = 0;
    #10 a = 1;  // should detect "101" → q = 1
    #10 a = 0;
    #10 a = 1;  // another "101"
    #10 a = 1;
    #10 a = 0;
    #10 a = 1;  // another "101"

    #20 $finish;
  end

endmodule
