`timescale 10 ns / 1 ns
module Quartus_FIFO_tb();
	reg SYSCLK, RST_B, WR_EN, RD_EN;
	reg [7:0]FIFO_IN; 
	wire FULL, EMPTY;
	wire [7:0]FIFO_OUT;
	
	always #5 SYSCLK = ~SYSCLK;
	initial begin
		SYSCLK=0; RST_B=1'b0; WR_EN=0; RD_EN=0; FIFO_IN=8'b0;
		#3 RST_B=1'b1;
		#11 RST_B=1'b0;
		#10 WR_EN=1'b1; FIFO_IN=8'd11;
		#10 FIFO_IN=8'd24;
		#10 FIFO_IN=8'd31;
		#10 FIFO_IN=8'd46;
		#10 FIFO_IN=8'd52;
		#10 FIFO_IN=8'd61; RD_EN=1'b1; //读写同步进行
		#10 FIFO_IN=8'd79;
		#10 FIFO_IN=8'd83;
		#10 FIFO_IN=8'd96;    			
		#10 WR_EN=1'b0; FIFO_IN=8'd0; 
		#70 RD_EN=1'b0;					
		#10 $stop; 
	end
	Quartus_FIFO U1(.clock(SYSCLK), .sclr(RST_B), .wrreq(WR_EN), .rdreq(RD_EN), 
						 .data(FIFO_IN), .full(FULL), .empty(EMPTY), .q(FIFO_OUT) );
endmodule 