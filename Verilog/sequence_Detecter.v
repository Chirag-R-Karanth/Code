module sequence_Detecter (
    input  wire a,
    input  wire clk,
    input  wire reset,
    output reg  q
);

    // State encoding
    parameter [1:0]
        S0 = 2'b00,
        S1 = 2'b01,
        S2 = 2'b10;

    reg [1:0] PS, NS;

    // -----------------------------
    // Next State Logic
    // -----------------------------
    always @(*) begin
        NS = PS; // default
        case (PS)
            S0: begin
                if (a) NS = S1;
                else   NS = S0;
            end

            S1: begin
                if (a) NS = S1;
                else   NS = S2;   // FIXED
            end

            S2: begin
                if (a) NS = S1;
                else   NS = S0;
            end

            default: NS = S0;
        endcase
    end

    // -----------------------------
    // State Register
    // -----------------------------
    always @(posedge clk) begin
        if (reset)
            PS <= S0;
        else
            PS <= NS;
    end

    // -----------------------------
    // Output Logic (Mealy)
    // -----------------------------
    always @(*) begin
        q = 1'b0; // default
        case (PS)
            S2: begin
                if (a) q = 1'b1; // detects 101
            end
            default: q = 1'b0;
        endcase
    end

endmodule
