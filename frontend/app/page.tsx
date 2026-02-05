import React from 'react';
import { Loader2, Plus } from "lucide-react"; 
import { Button } from "@/components/ui/button";
const AboutPage = () =>{
   return (
    // 3. JSX(HTML 모양의 코드) 반환
    <main className="p-8">
      <h1 className="text-2xl font-bold">OpenBlueprint Project</h1>
      <p className="mt-4 text-gray-600">
        Welcome
      </p>

      <div className="flex flex-col gap-4">
       { <Button>
          <Plus className="mr-2 h-4 w-4" /> 프로젝트 시작하기
        </Button> 
        }
      </div>
    </main>
  );
}

export default AboutPage;