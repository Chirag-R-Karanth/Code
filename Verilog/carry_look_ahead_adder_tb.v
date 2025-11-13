`timescale 1ns / 1ps

module carry_look_ahead_adder_tb();

    // Inputs
    reg [3:0] a;
    reg [3:0] b;
    reg       cin;

    // Outputs
    wire [3:0] sum;
    wire       cout;

    // Expected outputs
    reg [4:0] expected;

    // Instantiate the Unit Under Test (UUT)
    carry_look_ahead_adder dut (
        .a(a),
        .b(b),
        .cin(cin),
        .sum(sum),
        .cout(cout)
    );

    integer i, j, k;
    integer error_count = 0;

    initial begin
        $display("Starting Carry Lookahead Adder Testbench...");
        $display("Time\tA\tB\tCin\tSum\tCout\tExpected\tStatus");

        // Exhaustive test: all combinations of a, b, cin
        for (i = 0; i < 16; i = i + 1) begin
            for (j = 0; j < 16; j = j + 1) begin
                for (k = 0; k < 2; k = k + 1) begin
                    a = i[3:0];
                    b = j[3:0];
                    cin = k;

                    expected = a + b + cin;  // Reference addition

                    #10;  // Wait for outputs to settle

                    // Check result
                    if ({cout, sum} !== expected) begin
                        $display("%0t\t%h\t%h\t%b\t%h\t%b\t%h\t\tERROR",
                                 $time, a, b, cin, sum, cout, expected);
                        error_count = error_count + 1;
                    end else begin
                        $display("%0t\t%h\t%h\t%b\t%h\t%b\t%h\t\tPASS",
                                 $time, a, b, cin, sum, cout, expected);
                    end
                end
            end
        end

        // Final report
        $display("\n=== TEST COMPLETE ===");
        $display("Total errors: %0d", error_count);
        if (error_count == 0)
            $display("CLA PASSED all tests!");
        else
            $display("CLA FAILED %0d test cases!", error_count);

        $finish;
    end

    // Optional: Monitor for waveform viewing
    initial begin
        $dumpfile("cla_4bit.vcd");
        $dumpvars(0, tb_cla_4bit);
    end

endmodule
