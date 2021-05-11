Scanner sc= new Scanner(System.in)
int n=sc.nextInt();
String str = new String[n+1]
for(int i=1;i<=n;i++){
    str[i] = sc.nextLine();
}
int q = sc.nextInt();
while(q--){
    String s = br.readLine().split(" ");
    int[] arr = new int[s.length];
    for(int i=0;i<s.length;i++){
        arr[i] = Integer.partInt(s[i]);
    }
    String ans = "";
    for(int i=arr[0];i<=arr[1];i++){
        ans+=str[i];
    }
    Arrays.sort(ans);
    System.put.println(ans[arr[2]-1]);
}