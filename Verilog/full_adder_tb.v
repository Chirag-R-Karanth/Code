`timescale 1ns/1ps

module full_adder_tb();
    reg a ,b ,cin;
    wire sum ,cout;

    full_adder dut(sum, cout, a ,b, cin);
    initial begin
        a=0; b=0; cin=0;#5
        $display("sum=%b, cout=%b", sum, cout);
        #100 ;
        a=0; b=0; cin=1;#5
        $display("sum=%b, cout=%b", sum, cout);
        #100 ;
        a=0; b=1; cin=1;#5
        $display("sum=%b, cout=%b", sum, cout);
        #100 ;
        a=1; b=1; cin=1;#5
        $display("sum=%b, cout=%b", sum, cout);
        #100 $finish;
    end

    initial begin
        $dumpfile("full_adder.vcd");  // create a VCD file
        $dumpvars(0, full_adder_tb);
    end

endmodule
