`timescale 1ns/1ps;

module full_adder_tb();
    reg a ,b ,cin;
    wire sum ,cout;

    full_adder dut(sum, cout, a ,b, cin);
    initial begin
        //initial begin
            $monitor("time=%0t | a=%b b=%b cin=%b | sum=%b cout=%b",
                      $time, a, b, cin, sum, cout);

            a=0; b=0; cin=0;
            #10          cin=1;
            #10     b=1; cin=0;
            #10          cin=1;
            #10 a=1; b=0; cin=0;
            #10          cin=1;
            #10     b=1; cin=0;
            #10          cin=1;

            $finish;
            //end
    end

    initial begin
        $dumpfile("full_adder.vcd");  // create a VCD file
        $dumpvars(0, full_adder_tb);
    end

endmodule
