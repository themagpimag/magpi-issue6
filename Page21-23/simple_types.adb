with Ada.Text_IO;
use Ada.Text_IO;

procedure Simple_Types is
   X      :          Integer := 10;
   Y      : constant Integer := 20;
   Result :          Integer := 0;
begin
   Result := X + Y;

   Put_Line ("Result = " & Integer'Image (Result));
end Simple_Types;
