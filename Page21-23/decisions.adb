with Ada.Text_IO;
use Ada.Text_IO;

procedure Decisions is
   Is_Defective : Boolean := False;
begin
   if Is_Defective = True then
      Put_Line ("Defective");
   else
      Put_Line ("Not defective");
   end if;
end Decisions;

