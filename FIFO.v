module FIFO ( input SYSCLK, RST_B, WR_EN, RD_EN,
				  input [7:0]FIFO_IN, 
				  output FULL, EMPTY,
				  output reg [7:0]FIFO_OUT);
	reg [7:0] mem [0:3];					//定义存储器
	reg [2:0] r_addr, w_addr;			//读指针和写指针，增加一位校验位
	wire flag_w, flag_r;					//读写标志
	
	//读写功能实现
	always @(posedge SYSCLK or negedge RST_B)
		if (~RST_B) begin
			w_addr<=3'b0;r_addr <= 3'b0; FIFO_OUT<=3'bx;
		end
		else begin
			if(flag_w) begin
				mem[w_addr[1:0]] <= FIFO_IN;
				w_addr <= w_addr + 1'b1;
			end
			if(flag_r) begin
				FIFO_OUT <= mem[r_addr[1:0]];
				r_addr <= r_addr + 1'b1;
			end
			if(~flag_w && ~flag_r) begin
				r_addr<=r_addr;w_addr<=w_addr;FIFO_OUT<=FIFO_OUT;
			end
		end
	
	assign flag_w = (WR_EN && ~FULL) ? 1'b1 : 1'b0;
	assign flag_r = (RD_EN && ~EMPTY) ? 1'b1 : 1'b0;
	//溢出，空判断
	assign FULL = (w_addr[2] != r_addr[2] && w_addr[1:0] == r_addr[1:0]) ? 1'b1 : 1'b0;
	assign EMPTY = (w_addr[2] == r_addr[2] && w_addr[1:0] == r_addr[1:0]) ? 1'b1 : 1'b0;
endmodule			