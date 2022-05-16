`timescale 10 ns / 1 ns
module FIFO_tb();
	reg SYSCLK, RST_B, WR_EN, RD_EN;
	reg [7:0]FIFO_IN; 
	wire FULL, EMPTY;
	wire [7:0]FIFO_OUT;
	
	always #5 SYSCLK = ~SYSCLK;
	initial begin
		SYSCLK=0; RST_B=1'b1; WR_EN=0; RD_EN=0; FIFO_IN=8'b0;
		#3 RST_B=1'b0;
		#11 RST_B=1'b1;
		#10 WR_EN=1'b1; FIFO_IN=8'd11;
		#10 FIFO_IN=8'd24;
		#10 FIFO_IN=8'd31; RD_EN=1'b1; 
		#10 FIFO_IN=8'd46; 
		#10 FIFO_IN=8'd57;    			//写溢出
		#10 WR_EN=1'b0; FIFO_IN=8'd0; 
		#30 RD_EN=1'b0;					//400ns后发生读溢出
		#10 $stop;
	end
	
	FIFO U1(SYSCLK, RST_B, WR_EN, RD_EN, FIFO_IN, FULL, EMPTY, FIFO_OUT);
endmodule 